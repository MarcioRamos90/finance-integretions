import logging

from telegram.ext import (
    ApplicationBuilder,
)

from setup import TELEGRAM_TOKEN
from src.telegram_integration import (
    getfin_handler,
    getfinbydate_handler,
    newfin_handler,
    help_handler,
    unknown_handler,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


if __name__ == "__main__":
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    application.add_handler(getfin_handler)
    application.add_handler(getfinbydate_handler)
    application.add_handler(newfin_handler)
    application.add_handler(help_handler)
    application.add_handler(unknown_handler)

    application.run_polling()
