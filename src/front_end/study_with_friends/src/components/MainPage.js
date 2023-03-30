import React from "react";
import '../App.css';
import TopBar from './TopBar'
import StudySession from './StudySession'

function MainPage(props){
    return(
        <div id="mainPage">
            <TopBar />
            <hr class="solid-divider" />

            <div id="main-row">
                <div class="column" id="study-sessions">
                    <StudySession name="Jared" location="Laz's butt" time="1:40"/>
                    <StudySession name="Ivanna" location="Laz's butt"/>
                    <StudySession name="Laz" location="Will's butt"/>
                </div>
                <div class="column">
                    <p>google maps</p>
                </div>
            </div>
        </div>

    )
}

export default MainPage