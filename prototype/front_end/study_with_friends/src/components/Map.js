import React, {useState} from "react"
import GoogleMapReact from "google-map-react"
import LocationPin from "./LocationPin"
import "../style/Map.css"


const Map = ({ user, location1, location2, zoomLevel }) => {
  console.log('map: ' + user)
  return  (
      <div className="map">  
        <div className="google-map">
          <GoogleMapReact
            bootstrapURLKeys={{ key: 'AIzaSyB3lnX4Q5pHcsW_QGyNczyXfzWGVqIJHm8' }}
            // bootstrapURLKeys={{key: 'placeholder'}}
            defaultCenter={location1}
            defaultZoom={zoomLevel}
          >
            {user === null ? 
              <></> : (
                <LocationPin
                  lat={location1.lat}
                  lng={location1.lng}
                  text={location1.address}
                />
                
              )
            }
            {user === null ? 
              <></> : <LocationPin 
              lat={location2.lat}
              lng={location2.lng}
              text={location2.address}
            />
            }

          </GoogleMapReact>
        </div>
      </div>
    )
}

  export default Map