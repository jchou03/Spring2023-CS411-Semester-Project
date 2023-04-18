import React, { useState } from "react"
import Modal from "react-bootstrap/Modal"

function FriendDisplay (props){
    return (
        <div>
            <p>{props.name}</p>
        </div>
    )
}

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
                    return (<FriendDisplay name={friend.name} />)
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