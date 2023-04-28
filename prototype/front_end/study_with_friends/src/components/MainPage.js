import React, {useState, useEffect} from "react";

// import styling
import 'bootstrap/dist/css/bootstrap.min.css';
import '../style/App.css';

// react boostrap imports
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal'
import Form from 'react-bootstrap/Form'

// other imports
import axios from "axios";
import FacebookLogin from 'react-facebook-login'

// other components
import TopBar from './TopBar'
import StudySession from './StudySession'
import Studying from "./Studying"
import SignIn from "./SignIn"
import Map from "./Map"
// can use modals for sign in/sign up instead of using using react-router-dom with separate pages
// import { 
//     BrowserRouter as Router,
//     Switch, 
//     Route, 
//     Redirect, 
// } from "react-router-dom"

// facebook oauth login
// import facebook

// updated data structure, link study sessions to the friends, so pull the list of friends, then check if they have study sessions 
var friends = [
    {
        id:1,
        name:"Jared",
        studyingNow: true,
        studySession: {
            location:"GSU",
            time:"11:20"
        }
    },
    {
        id:2,
        name:"Spencer",
        studyingNow: true,
        studySession: {
            location:"Questrom",
            time:"1:45"
        }
    },
    {
        id:3,
        name:"Bowen",
        studyingNow: true,
        studySession: {
            location:"CDS",
            time:"2:15"
        }
    },
]

// test object to hold a location
const testLocation = {
    address: 'Boston, MA 02215',
    lat: 42.35085737795678,
    lng: -71.10533494442352,
}

const zoomDefault = 15;

function MainPage(props){
    // facebook login object
    const [user, setUser] = useState(null);

    const responseFacebook = (response) => {
        console.log(response)
    }

    // hooks to determine the display status of the modal with sign in/sign up pages
    const [signInDisplay, setSignInDisplay] = useState(false);
    const [signUpDisplay, setSignUpDisplay] = useState(false);

    // hook to determine the study status of the user
    const [studying, setStudying] = useState(false);
    // function to stop the study session
    const stopStudying = () => {
        // calculate study time here (later)
        setStudying(false);
    }

    // hooks to keep track of the modal display status
    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleOpen = () => setShow(true);
    
    // hooks to handle the form inputs for starting a study session
    const [studyLocation, setStudyLocation] = useState("")
    const [studyEndTime, setStudyEndTime] = useState("")

    // function to handle the submit of the modal form
    const handleSubmit = () => {
        console.log("study location: " + studyLocation)
        console.log("study until time: " + studyEndTime)
        setStudying(true)
        handleClose()
    }

    // test of connecting to the backend access
    useEffect(() => {
        axios.get('http://127.0.0.1:5000/').then(response => {
            console.log("SUCCESS" , response)
        }).catch(error => {
            console.log(error)
        })
    })

    return(
        <div id="mainPage">
            <TopBar setDisplay={setSignInDisplay} user={user} setUser={setUser} friends={friends}/>
            
            {/* sign in/sign up modal */}
            <SignIn show={signInDisplay} user={user} setUser={setUser} handleClose={() => setSignInDisplay(false)}/>
            
            <hr class="solid-divider" />

            {/* display a bar to show study progress (when studying) */}
            {studying ? (<Studying location={studyLocation} time={studyEndTime} onClick={stopStudying}/>) : <></>}

            <div id="main-row">
                <div class="column" id="study-sessions">
                    {friends.map((friend) => {
                        if(friend.studyingNow){
                            return (<StudySession key={friend.id} name={friend.name} location={friend.studySession.location} time={friend.studySession.time}/>)
                        }else{
                            return <></>
                        }
                    })}
                </div>
                <div class="column">
                    <Button id="study-button" onClick={handleOpen}>
                        Study Now
                    </Button>

                    {/* Modal to pop up when you click to start a study session */}
                    <Modal
                        show={show}
                        keyboard={true}
                        onEscapeKeyDown={handleClose}
                        backdrop={true}
                        onHide={handleClose}
                    >
                        <Modal.Header closeButton>
                            <Modal.Title>Start a Study Session</Modal.Title>
                        </Modal.Header>
                        <Modal.Body>
                            <Form>
                                <Form.Group >
                                    <Form.Label>Where do you want to study?</Form.Label>
                                    <Form.Control placeholder="Boston University" onChange={(event) => {setStudyLocation(event.target.value)}}/>
                                </Form.Group>

                                <Form.Group>
                                    <Form.Label>When do you want to finish studying?</Form.Label>
                                    <Form.Control type="time" onChange={(event) => setStudyEndTime(event.target.value)}></Form.Control>
                                </Form.Group>
                            </Form>
                        </Modal.Body>
                        <Modal.Footer>
                            <Button variant="secondary" onClick={handleClose}>
                                Cancel
                            </Button>
                            <Button variant="primary" onClick={handleSubmit}>
                                Start Study Session!
                            </Button>
                        </Modal.Footer>
                    </Modal>

                    <Map location={testLocation} zoomLevel={zoomDefault}/>
                </div>
            </div>
        </div>
    )
}


export default MainPage

