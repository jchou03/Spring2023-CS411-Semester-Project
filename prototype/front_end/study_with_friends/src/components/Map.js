import React, {useState} from "react"
import GoogleMapReact from "google-map-react"
import LocationPin from "./LocationPin"
import "../style/Map.css"


const Map = ({ location, zoomLevel }) => (
    <div className="map">  
      <div className="google-map">
        <GoogleMapReact
          bootstrapURLKeys={{ key: 'temporarily add here without committing it while backend isn\'t ready yet' }}
          defaultCenter={location}
          defaultZoom={zoomLevel}
        >
          <LocationPin
            lat={location.lat}
            lng={location.lng}
            text={location.address}
          />
        </GoogleMapReact>
      </div>
    </div>
  )

  export default Map