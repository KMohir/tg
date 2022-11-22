from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard=ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Нажмите чтобы отправить местоположение",
                       request_location=True

                       )
        ],

    ],
    resize_keyboard=True
)


keyboardcontakt=ReplyKeyboardMarkup(

    keyboard=[[

        KeyboardButton(text="Nomeringizni ni yubormoqchi bolsangiz shuni bosasiz ",
                       request_contact=True

                       )
        ],

    ],resize_keyboard=True

)

keyboardstart=ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Oficgacha_masofa",

                       )
        ],


    ],
    resize_keyboard=True
)
