from telegram import Update
from telegram.ext import ContextTypes
from bot.utils import get_text

"""
Simple per-user task list stored in `context.user_data`.

This module implements a minimal to-do feature:
- /add <text>   — append a new task
- /list         — show all tasks with status
- /done <id>    — mark task as done
- /stats        — show counts (total/done)

Tasks are kept in memory per user via `Application` persistence, so they survive
bot restarts when `PicklePersistence` is enabled.
"""

async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Add a new task from the command arguments.

    Usage:
        /add buy bread

    Behavior:
        - If no arguments are provided, replies with usage text.
        - Otherwise, appends a dict `{"text": ..., "done": False}` to `user_data["tasks"]`.

    Args:
        update: Telegram update.
        context: Callback context with `user_data` and `args`.
    """
    lang = context.user_data.get("language", "en")  
    if not context.args:
        await update.message.reply_text(get_text("add_usage", lang))
        return

    task_text = " ".join(context.args)
    tasks = context.user_data.setdefault("tasks", [])
    tasks.append({"text": task_text, "done": False})

    await update.message.reply_text(f"{get_text('task_added', lang)} ({len(tasks)}) ✅")

async def list_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    List all tasks with a check/cross mark.

    Shows a numbered list: `1. <text> ✔️/❌`.
    Replies with a "no tasks" message if the list is empty.

    Args:
        update: Telegram update.
        context: Callback context.
    """
    lang = context.user_data.get("language", "en")
    tasks = context.user_data.get("tasks", [])
    if not tasks:
        await update.message.reply_text(get_text("no_tasks", lang))
        return

    lines = []
    for idx, t in enumerate(tasks, 1):
        status = "✔️" if t["done"] else "❌"
        lines.append(f"{idx}. {t['text']} {status}")
    await update.message.reply_text("\n".join(lines))

async def done_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Mark a task as done by its 1-based index.

    Usage:
        /done 2

    Behavior:
        - Validates that the first argument is a digit and points to an existing task.
        - Sets `task["done"] = True` when found; otherwise informs that no such task.

    Args:
        update: Telegram update.
        context: Callback context.
    """
    lang = context.user_data.get("language", "en")
    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text(get_text("done_usage", lang))
        return

    idx = int(context.args[0]) - 1
    tasks = context.user_data.get("tasks", [])

    if 0 <= idx < len(tasks):
        tasks[idx]["done"] = True
        await update.message.reply_text(get_text("task_done", lang).format(idx=idx+1))
    else:
        await update.message.reply_text(get_text("no_task", lang))

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Show total and completed task counters.

    Counts tasks in `user_data["tasks"]` and replies with two lines:
        Total: <n>
        Done:  <m>

    Args:
        update: Telegram update.
        context: Callback context.
    """
    lang = context.user_data.get("language", "en")
    tasks = context.user_data.get("tasks", [])
    done = sum(t["done"] for t in tasks)
    total = len(tasks)
    await update.message.reply_text(
        f"{get_text('total_tasks', lang)} {total}\n{get_text('done_tasks', lang)} {done}"
    )
