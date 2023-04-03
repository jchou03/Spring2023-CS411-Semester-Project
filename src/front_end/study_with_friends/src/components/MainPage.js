import React, {useState} from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import '../style/App.css';
import TopBar from './TopBar'
import StudySession from './StudySession'
import Studying from "./Studying"

// react boostrap imports
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal'
import Form from 'react-bootstrap/Form'


// this array of study sessions will
var studySessions = [
    {
        name:"Jared",
        location:"GSU",
        time:"11:20"
    },
    {
        name:"Spencer",
        location:"Questrom",
        time:"1:45"
    },
    {
        name:"Bowen",
        location:"CDS",
        time:"2:15"
    }
]


function MainPage(props){
    // hook to determine the study status of the user
    const [studying, setStudying] = useState(false);

    // hooks to keep track of the modal display status
    const [show, setShow] = useState(false)
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

    return(
        <div id="mainPage">
            <TopBar />
            
            <hr class="solid-divider" />

            {/* display a bar to show study progress (when studying) */}
            {studying ? (<Studying location={studyLocation} time={studyEndTime}/>) : <></>}

            <div id="main-row">
                <div class="column" id="study-sessions">
                    {studySessions.map((details) => {
                        return (<StudySession name={details.name} location={details.location} time={details.time}/>)
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




                    <p>google maps</p>
                </div>
            </div>
        </div>


    )
}


export default MainPage

