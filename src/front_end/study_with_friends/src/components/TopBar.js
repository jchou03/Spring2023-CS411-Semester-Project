import React from "react";
import '../style/App.css';
import '../style/TopBar.css'
import Button from 'react-bootstrap/Button'

function TopBar (props) {
    var username = "YDD Laz"
    return (
        <div id="topbar">
            <h1>Study Finder</h1>
            <div>
                {/* can add a profile picture in top right later */}
                {username === "" ? (<Button variant="primary">Sign In</Button>) : (<div class="right-side"><p>Hello {username}</p> <Button variant="Primary">Sign Out</Button></div>)}
            </div>
        </div>
    )
}

export default TopBar