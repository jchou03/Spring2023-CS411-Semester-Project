import React, {useState} from "react"

import 'bootstrap/dist/css/bootstrap.min.css'
import Modal from 'react-bootstrap/Modal'
import Form from 'react-bootstrap/Form'

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
                Oauth Sign In Button Here
            </Modal.Body>
        </Modal>
    )
}

export default SignIn