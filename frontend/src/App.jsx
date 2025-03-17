import { useState, useEffect } from 'react'
import ContactList from './ContactList'
import './App.css'

function App() {
  const [contacts, setContacts] = useState([
    {
      "id": 1,
      "firstName": "Bob",
      "lastName": "Barter",
      "email": "bb@gmail.com"
    }])

  // as soon as the component renders run func and get data
  useEffect(() => {
    // fetchContacts()
  }, [])

  const fetchContacts = async () => {
    const response = await fetch("http://127.0.0.1:5000/contacts")
    const data = await response.json()
    setContacts(data.contacts)
    console.log(data.contacts)
  }

  return <ContactList contacts={contacts} />
}

export default App
