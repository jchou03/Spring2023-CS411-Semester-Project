import React, {useState} from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import '../style/App.css';
import TopBar from './TopBar'
import StudySession from './StudySession'
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal'


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
    // hooks to keep track of the modal display status
    const [show, setShow] = useState(false)
    const handleClose = () => setShow(false);
    const handleOpen = () => setShow(true);


    return(
        <div id="mainPage">
            <TopBar />
            <hr class="solid-divider" />


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
                        <Modal.Body>Let's start studying! </Modal.Body>
                        <Modal.Footer>
                            <Button variant="secondary" onClick={handleClose}>
                                Cancel
                            </Button>
                            <Button variant="primary" onClick={handleClose}>
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

