from fastapi import FastAPI, HTTPException, status
from fastapi import APIRouter
from schemas import (
    User,
    Admin,
    users_dictionary,
    User_response,
    Admin_response,
    admin_dictionary,
)
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="logs.log",
    filemode="w",
    format="%(asctime)s-%(levelname)s-%(message)s",
)
"""
logging.debug("this is DEBUG message!")
logging.info("this is INFO message!")
logging.warning("this is WARNING message!")
logging.error("This is ERROR message!")
logging.critical("this is CRITICAL message!")
"""
app = FastAPI()

router = APIRouter()


# CREATE THE USER(POST-METHOD
@router.post(
    "/POST_USER/{id}",
    response_model=User_response,
    response_description="POST_METHOD",
    status_code=status.HTTP_201_CREATED,
    summary="Create an User",
    tags=["User"]
)
async def Create_USER(id: int, request: User):
    if id in users_dictionary:
        logging.error("already used this user id")
        raise HTTPException(status_code=status.HTTP_226_IM_USED)
    logging.info("added the User")
    result = users_dictionary[id] = request
    return result


"""
post method 
{id}-router id is a path parameter
response_model- if response successfully show request body
response_description-if response successfully show description
status_code-if response successfully show the status_code number(201)
summary-show the summary on router (Docs)

fun():
id is a path parameter datatype int
request is a query parameter: base model of user
if id  in dictionary throw HTTPException
if(not in) dictionary added the user in dictionary
"""


# GET THE USER(GET)-METHOD
@router.get(
    "/GET_USER{id}",
    response_model=User_response,
    response_description="GET_METHOD",
    status_code=status.HTTP_200_OK,
    summary="Get an User",
    tags=["User"],
)
async def Get_User(id: int):
    if id not in users_dictionary:
        logging.warning("user id not in user_dictionary")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    logging.info("show successfuly user!")
    result = users_dictionary[id]
    return result


"""
{id}-router id is a path parameter
response_model- if response successfully show request body
response_description-if response successfully show description
status_code-if response successfully show the status_code number(200)
summary-show the summary on router (Docs)

fun():
id is a path parameter datatype int
if id not in Dictionary throw message HTTPException(404-NOT_FOUND)
otherwise show the user
"""


# UPDATE THE USER(PUT)-METHOD
@router.put(
    "/UPDAE_USER{id}",
    response_model=User_response,
    response_description="PUT_METHOD",
    status_code=status.HTTP_201_CREATED,
    summary="Update an User",
    tags=["User"],
)
async def Update_User(id: int, request: User_response):
    if id not in users_dictionary:
        logging.warning("user id not in user_dictionary")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    logging.info("update successfuly user!")
    result = users_dictionary[id] = request
    return result


"""
{id}-router id is a path parameter
response_model- if response successfully show request body
response_description-if response successfully show description
status_code-if response successfully show the status_code number(201)
summary-show the summary on router (Docs)

fun():
id is a path parameter datatype int
request is a query parameter: base model of user
if id not in user dictionary throw message HTTPexceptio(404_NOT_FOUND)
otherwise id in dictionary update the user
"""


# DELETE THE USER(DELETE)-METHOD
@router.delete(
    "/DELETE_USER{id}",
    response_description="Deleted",
    summary="Delete an User",
    tags=["User"],
)
async def Delete_User(id: int):
    if id not in users_dictionary:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    del users_dictionary[id]
    logging.info("deleted successfuly user!")
    return {"deleted successfully"}


"""
{id}-router id is a path parameter
response_description-if response successfully show description
summary-show the summary on router (Docs)

if id not in user dictionary throw message HTTPException(404_NOT_FOUND)
otherwise id in user dictionary deleted user 
throw message "deleted successfully"

"""
# __________________________________________________________________________________________________________________________#


# CREATE THE ADMIN(POST-METHOD)
@router.post(
    "/POST_ADMIN/{id}",
    response_model=Admin_response,
    response_description="POST_METHOD",
    status_code=status.HTTP_201_CREATED,
    summary="Create an Admin",
    tags=["Admin"],
)
async def Create_Admin(id: int, request: Admin):
    if id in admin_dictionary:
        logging.error("already used this user id")
        raise HTTPException(status_code=status.HTTP_226_IM_USED)
    logging.info("added the Admin")
    result = admin_dictionary[id] = request
    return result


"""
id-is a path parameter
response_model- if response successfully show request body
response_description-if response successfully show description
status_code-if response successfully show the status_code number(201)
summary-show the summary on router (Docs)

fun():
id is a path parameter datatype int
request is a query parameter: base model of Admin
if id  in dictionary throw HTTPException
otherwise  added the Admin in dictionary



"""


# GET THE ADMIN(GET)-METHOD
@router.get(
    "/GET_ADMIN/{id}",
    response_model=Admin_response,
    response_description="GET_METHOD",
    status_code=status.HTTP_200_OK,
    summary="Get an Admin",
    tags=["Admin"],
)
async def Get_Admin(id: int):
    if id not in admin_dictionary:
        logging.warning(" id not in admin_dictionary")
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    logging.info("show successfuly admin!")
    result = admin_dictionary[id]
    return result


"""
id-is a path parameter
response_model- if response successfully show request body
response_description-if response successfully show description
status_code-if response successfully show the status_code number(200)
summary-show the summary on router (Docs)

fun():
id is a path parameter datatype int
if id not in Dictionary throw message HTTPException(404-NOT_FOUND)
otherwise show the admin

"""


# UPDATE THE ADMIN(PUT)-METHOD
@router.put(
    "/UPDAE_ADMIN{id}",
    response_model=Admin_response,
    response_description="PUT_METHOD",
    status_code=status.HTTP_201_CREATED,
    summary="Update an Admin",
    tags=["Admin"],
)
async def Update_Admin(id: int, request: Admin):
    if id not in admin_dictionary:
        logging.warning("id not in admin_dictionary")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    logging.info("update successfuly Admin!")
    result = admin_dictionary[id] = request
    return result


"""
id-is a path parameter
response_model- if response successfully show request body
response_description-if response successfully show description
status_code-if response successfully show the status_code number(201)
summary-show the summary on router (Docs)
fun():
id is a path parameter datatype int
if id not in Dictionary throw message HTTPException(404-NOT_FOUND)
otherwise show the updated admin


"""


# DELETE THE ADMIN(DELETE)-METHOD
@router.delete(
    "/DELETE_ADMIN/{admin_id}",
    response_description="Deleted",
    summary="Delete an Admin",
    tags=["Admin"],
)
async def Delete_Admin(id: int):
    if id not in admin_dictionary:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    del admin_dictionary[id]
    logging.info("deleted successfuly Admin!")
    return {"deleted successfully"}


"""
{id}-router id is a path parameter
response_description-if response successfully show description
summary-show the summary on router (Docs)

if id not in user dictionary throw message HTTPException(404_NOT_FOUND)
otherwise id in admin dictionary deleted  admin
throw message "deleted successfully"

"""


app.include_router(router=router)
