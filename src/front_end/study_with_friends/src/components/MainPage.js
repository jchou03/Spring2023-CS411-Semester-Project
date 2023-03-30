import React from "react";
import '../style/App.css';
import TopBar from './TopBar'
import StudySession from './StudySession'

function MainPage(props){
    return(
        <div id="mainPage">
            <TopBar />
            <hr class="solid-divider" />

            <div id="main-row">
                <div class="column" id="study-sessions">
                    <StudySession name="Jared" location="Questrom" time="1:40"/>
                    <StudySession name="Ivanna" location="GSU"/>
                    <StudySession name="Laz" location="Warren Towers"/>
                </div>
                <div class="column">
                    <div id="study-button">
                        <p>Study Now</p>
                    </div>
                    <p>google maps</p>
                </div>
            </div>
        </div>

    )
}

export default MainPage