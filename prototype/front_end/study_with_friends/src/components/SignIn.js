import React, {useState} from "react"

import 'bootstrap/dist/css/bootstrap.min.css'
import Modal from 'react-bootstrap/Modal'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

function SignIn(props){
    // hook to keep track of the inputted username
    const [name, setName] = useState("")

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
                <Form>
                    <Form.Group>
                        Oauth Sign In Goes Here
                    </Form.Group>
                </Form>
            </Modal.Body>
            <Modal.Footer>
                <Button variant="primary" onClick={props.handleClose}>
                    Sign In Using OAuth
                </Button>
            </Modal.Footer>
        </Modal>
    )
}

export default SignIn