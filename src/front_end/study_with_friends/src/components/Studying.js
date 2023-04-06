import React, {useState} from "react"
import '../style/Studying.css'
import CloseButton from 'react-bootstrap/CloseButton'

function Studying (props){
    return (
        <div id="studying-container">
            <CloseButton onClick={props.onClick}/>
            <h1>You're studying at {props.location} until {props.time}</h1>
        </div>
    )
}

export default Studying