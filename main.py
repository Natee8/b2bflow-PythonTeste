from services.supabase import searchContacts
from services.zapiService import sendMessage
from utils.formatter import format_phone
from models.IPeople import IPeople

def main(): 
    contacts = searchContacts()

    for contact in contacts:
        person = IPeople(
            name=contact["name"],
            phone=format_phone(contact["phone"])
        )

        result = sendMessage(person.name, person.phone)
        print(result)

if __name__ == "__main__":
    main()
