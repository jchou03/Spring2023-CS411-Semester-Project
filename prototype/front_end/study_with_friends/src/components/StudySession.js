import React from "react";
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

export default StudySession