from fastapi import FastAPI

main_app = FastAPI()


@main_app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}


@main_app.get("/user/admin")
async def wel_adm() -> dict:
    return {"message": "Вы вошли как администратор"}

@main_app.get("/user")
async def usr_info(username: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

@main_app.get("/user/{user_id}")
async def wel_usr(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}
