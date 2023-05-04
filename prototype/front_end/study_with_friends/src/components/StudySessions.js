import React, {useState} from 'react'
import "../style/App.css"
import "../style/StudySession.css"

function StudySession(props){
    return(
        <div class="study-session">
            <p>{props.name} is studying at {props.location}</p>
            {/* need to implement the time font */}
            <p class="time">{props.time != null ? ("until " + props.time) : ""}</p>
        </div>
    )
}

function StudySessions ({ user, friends }) {
    console.log("friends " + friends)
    for (var i = 0; i < friends.length; i++){
        console.log(friends[i])
    }

    return (
        (user !== null ? (friends.length !== 0 ? (friends.map((friend) => {
            if(friend[8] === 1){
                return (<StudySession key={friend.id} name={friend[0]}  location={friend[6]} time={friend[7]}/>)
            }else{
                return <></>
            }
        })) : <p>Go get some friends</p>) : <p>Sign in to use the app!</p>) 
    )
}

export default StudySessions