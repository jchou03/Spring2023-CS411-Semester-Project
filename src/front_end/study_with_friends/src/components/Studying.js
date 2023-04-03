import React, {useState} from "react"

function Studying (props){
    return (
        <div>
            <h1>You're studying at {props.location} until {props.time}</h1>
        </div>
    )
}

export default Studying