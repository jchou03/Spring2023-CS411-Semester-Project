import React, {useState} from 'react'
import StudySession from './StudySession'

function StudySessions ({ user, friends }) {
    console.log("friends " + friends)
    for (var i = 0; i < friends.length; i++){
        console.log(friends[i])
    }

    return (
        (user != null ? (friends.length != 0 ? (friends.map((friend) => {
            if(friend[8] == true){
                return (<StudySession name={friend[0]}  location="test"/>)
            }
        })) : <p>Go get some friends</p>) : <p>Sign in to use the app!</p>) 
    )
}

export default StudySessions