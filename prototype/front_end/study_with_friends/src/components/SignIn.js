import React, {useState} from "react"
import axios from 'axios'
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

    // function to update the user when a user is logged in
    const responseFacebook = async (response) => {
        console.log(response)
        // check if a user does exist, and if it doesn't, create a new user in the database
        var params = {'id':response.id}
        params.headers.add('Access-Control-Allow-Origin', '*')
        var login_res = await axios.post('http://127.0.0.1:5000/login', params)
        console.log("login res is : " + login_res)
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