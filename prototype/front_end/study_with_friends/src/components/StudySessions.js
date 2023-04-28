import React, {useState} from 'react'
import StudySession from './StudySession'

function StudySessions ({ user, friends }) {
    console.log("friends " + friends)

    return (
        (user != null ? (friends.length != 0 ? (<p>you have friends</p>) : <p>Go get some friends</p>) : <p>Sign in to use the app!</p>) 
    )
}

export default StudySessions