import logging
from telegram import Update
from telegram.ext import (
    filters,
    MessageHandler,
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

from data import get_all_finances, new_finance_item, get_list_by_day
from setup import TELEGRAM_TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Sorry, I didn't understand that command.",
    )


async def getfin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    finances = await get_all_finances()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=finances)


async def getfinbydate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    finances = await get_list_by_day()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=finances)


async def newfin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = await new_finance_item(update.message.text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    value = update.message.text.partition(" ")[2]
    usage = (
        "Bem vindo ao menu de ajuda de PersonalFinances!\n"
        "--------------------------------------------\n"
        "getfin -> devolve items e soma dos items\n"
        "newfin -> cria novo item de financa"
    )
    if value == "newfin":
        usage = (
            "cria novo item de financa\n"
            "ex: newfin -valor 10.01 -data hoje -descricao Compras mercadinho\n"
            "--------------------------------------------\n"
            "-valor ou -v -> recebe apenas valores númericos\n"
            "-dia ou -d -> recebe uma data ex: 10/03/2022\n"
            "-descricao ou -desc -> recebe um texto\n"
        )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=usage)


if __name__ == "__main__":
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    getfin_handler = CommandHandler("getfin", getfin)
    newfin_handler = CommandHandler("newfin", newfin)
    getfinbydate_handler = CommandHandler("gbydate", getfinbydate)

    help_handler = CommandHandler("help", help)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(getfin_handler)
    application.add_handler(getfinbydate_handler)
    
    application.add_handler(newfin_handler)

    application.add_handler(help_handler)
    application.add_handler(unknown_handler)

    application.run_polling()
