import React, { useState } from "react"
import Button from 'react-bootstrap/Button'
import "../style/Friend.css"


function FriendUnit({friend}){
    return (
        <div id="friend-unit" onMouseOver={console.log("hovering")}>
            <p>{friend.name}</p>
            {friend.studying ? (<p>Studying!</p>) : (<p>insert total study time here</p>)}
        </div>
    )
}

function FriendDisplay(props){
    console.log("friend props object: " + props.friend)
    return (
        <div>
            {props.friends.map((friend) => {
                return <FriendUnit friend={friend} key={friend.id}/>
            })}
        </div>
    )
}

export default FriendDisplay