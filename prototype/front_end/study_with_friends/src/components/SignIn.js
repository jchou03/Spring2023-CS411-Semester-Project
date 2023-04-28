import React, {useState} from "react"

// bootstrap imports
import 'bootstrap/dist/css/bootstrap.min.css'
import Modal from 'react-bootstrap/Modal'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

// facebook imports
import FacebookLogin from 'react-facebook-login'

function SignIn(props){
    // hook to keep track of the inputted username
    const [name, setName] = useState("")

    // need to add a function to update the username based on the logged in user
    const responseFacebook = (response) => {
        console.log(response)
        props.setUser(response)
        props.handleClose()
    }

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
                        {/* facebook login button */}
                        <FacebookLogin
                            appId="135421432654185"
                            autoLoad={true}
                            fields="name,email,picture"
                            onClick={() => {console.log("clicked")}}
                            callback={responseFacebook} />
                    </Form.Group>
                </Form>
            </Modal.Body>
            {/* <Modal.Footer>
                <Button variant="primary" onClick={props.handleClose}>
                    Sign In Using OAuth
                </Button>
            </Modal.Footer> */}
        </Modal>
    )
}

export default SignIn