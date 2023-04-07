import React, {useState} from "react"
import Modal from 'react-bootstrap/Modal'
import 'bootstrap/dist/css/bootstrap.min.css'

function SignIn(props){
    return(
        <Modal
            show={props.show}
            keyboard={true}
            onEscapeKeyDown={props.handleClose}
            backdrop={true}
            onHide={props.handleClose}
        >
            <Modal.Header>
                <Modal.Title>
                    Sign In Using OAuth
                </Modal.Title>
            </Modal.Header>
            <Modal.Body>
                test
            </Modal.Body>
            <Modal.Footer>
                test
            </Modal.Footer>
            </Modal>
    )
}

export default SignIn