import { Icon } from '@iconify/react'

function LocationPin (props){
    return (
        <div className='pin'>
            <Icon icon={"ph:map-pin-fill"} className="pin-icon" />
            <p className='pin-text'>{props.text}</p>
        </div>
    )
}

export default LocationPin