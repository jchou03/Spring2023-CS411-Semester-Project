import React, {useState} from "react";
import '../style/App.css';
import '../style/TopBar.css'
import { Button, Form, Modal } from 'react-bootstrap'
import FriendDisplay from "./Friend";
import 'bootstrap/dist/css/bootstrap.min.css';

function TopBar (props) {
    console.log(props.setDisplay)
    const [username, setUsername] = useState("Laz")

    // hook for showing friend modal
    const [show, setShow] = useState(false)
    const handleClose = () => setShow(false);
    const handleOpen = () => setShow(true);

    const signOut = () => {
        setUsername("")
    }

    const signIn = () => {
        props.setDisplay(true)
        setUsername("Laz")
    }

    return (
        <div id="topbar">
            <h1>Study Finder</h1>
            <div>
                {/* can add a profile picture in top right later */}
                {/* custom right side depending on if the user is signed in or not */}
                
                {username === "" ? 
                    (<div class="right-side">
                        <Button variant="primary" onClick={signIn}>Sign In</Button>
                        {/* <Button variant="primary" onClick={signIn}>Sign Up</Button> */}
                    </div>) : 
                    (<div class="right-side">
                        <p>Hello {username}</p>
                        <Button variant="light" onClick={handleOpen}>Friends</Button>
                        <Button variant="primary" onClick={signOut}>Sign Out</Button>
                    </div>)
                }
            </div>

            {/* modal for showing list of friends */}
            <Modal
                show={show}
                keyboard={true}
                onEscapeKeyDown={handleClose}
                backdrop={true}
                onHide={handleClose}
            >
                <Modal.Header closeButton>
                    <Modal.Title>Friend List</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <FriendDisplay friends={props.friends}/>
                </Modal.Body>
            </Modal>


        </div>
    )
}

export default TopBar