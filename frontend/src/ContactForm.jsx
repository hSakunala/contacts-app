import { useState } from "react";

// get existing contact as parameter if editing contact
const ContactForm = ({ existingContact = {}, updateCallback }) => {
    // useStates for all data entry in form
    const [firstName, setFirstName] = useState(existingContact.firstName || "")
    const [lastName, setLastName] = useState(existingContact.lastName || "")
    const [email, setEmail] = useState(existingContact.email || "")

    const updating = Object.entries(existingContact).length !== 0

    const onSubmit = async (e) => {
        e.preventDefault()

        // get data from form through useState variables
        const data = {
            firstName,
            lastName,
            email
        }
        // depending if updating is true or false, change url endpoint
        const url = "http://127.0.0.1:5000/" + (updating ? `update_contact/${existingContact.id}` : "create_contact")
        const options = {
            // if updating change api fetch method
            method: updating ? "PATCH": "POST",
            headers: {
                "Content-Type" : "application/json"
            },
            body: JSON.stringify(data)
        }
        // use url and options to make new entry in db
        const response = await fetch(url,options)
        
        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json()
            alert(data.message)
        }else{
            // tell app it finished create or update function and close modal
            updateCallback()
        }
    }

    return ( 
        <form onSubmit={onSubmit}>
            <div>
                <label htmlFor="firstName">First Name:</label>
                <input
                    type="text"
                    id="firstName"
                    value={firstName}
                    onChange={(e) => setFirstName(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="lastName">Last Name:</label>
                <input
                    type="text"
                    id="lastName"
                    value={lastName}
                    onChange={(e) => setLastName(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="email">Email:</label>
                <input
                    type="text"
                    id="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
            </div>
            <button type="submit">{updating ? "Update" : "Create"}</button>
        </form>
    )
};

export default ContactForm