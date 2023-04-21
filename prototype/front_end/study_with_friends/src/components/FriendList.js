import React, { useState } from "react"
import Modal from "react-bootstrap/Modal"

function FriendDisplay ({name, studyingNow, studySession}){
    return (
        <div>
            <p>{name}</p>
        </div>
    )
}

// get an array of friend objects in props

function FriendList (props){
    return (
        <Modal>
            show={props.show}
            keyboard={true}
            onEscapeKeyDown={props.handleClose}
            backdrop={true}
            onHide={props.handleClose}
            <Modal.Header>
                <Modal.Title>
                    Friend List
                </Modal.Title>
            </Modal.Header>
            <Modal.Body>
                {/* insert mapping of friends to display */}
                {props.friends.map((friend) => {
                    return (<FriendDisplay friend={friend} />)
                })}
            </Modal.Body>
            <Modal.Footer>
                <Button variant="primary" onClick={props.handleClose}>
                    Close
                </Button>
            </Modal.Footer>
        </Modal>
    )
}