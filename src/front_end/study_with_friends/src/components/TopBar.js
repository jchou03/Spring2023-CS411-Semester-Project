import React from "react";
import '../style/App.css';


function TopBar (props) {
    var username = "YDD Laz"
    return (
        <div id="topbar">
            <h1>Study Finder</h1>
            <div>
                {/* can add a profile picture in top right later */}
                <p>Hello {username}</p>
            </div>
        </div>
    )
}

export default TopBar