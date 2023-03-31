import React, {useState} from "react";
import '../style/App.css';
import '../style/TopBar.css'
import Button from 'react-bootstrap/Button'
import 'bootstrap/dist/css/bootstrap.min.css';

function TopBar (props) {
    const [username, setUsername] = useState("Laz")

    const signOut = () => {
        setUsername("")
    }

    const signIn = () => {
        setUsername("Laz")
    }

    return (
        <div id="topbar">
            <h1>Study Finder</h1>
            <div>
                {/* can add a profile picture in top right later */}
                {/* custom right side depending on if the user is signed in or not */}
                {username === "" ? 
                    (<Button variant="primary" onClick={signIn}>Sign In</Button>) : 
                    (<div class="right-side">
                        <p>Hello {username}</p> 
                        <Button variant="primary" onClick={signOut}>Sign Out</Button>
                    </div>)
                }
            </div>
        </div>
    )
}

export default TopBar