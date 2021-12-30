# NOVEL MAP CUSTOMIZER
#### Video Demo:  <https://youtu.be/L4IyMEsLlDQ>
#### Description:
  This helps authors to customize the maps for their novel specifying where a particular place is located on the map.
  They can specify areas , pinpoint locations and describe each of these places to readers intrested in gaining more insight about places in the book
  they are reading .
  The geospartial elements are stored using postgis (a spatial database extender for PostgreSQL). The map is rendered with a javascript library using leaflet ,the 
  controllers(backend) is handled with django and django restframework for its api. The djangorestframework helps with easy parsing and representation of the locations in geojson.
### Design
  The model file creates a database for the author , Book and the locations for the map points to be stored.
  The view on the other hand acts as the controller , this is where the logic resides and the files accepted are handled.
  The forms allows to validate the submitted user input and allows for easy storage of these inputs.
  the api helps to render the map points in geojson.
  leaflet library helps handle the map rendering and basic event listeners .
  boostrap  is used for the design in place of oveload css.
  
 ### Why Build This ?
    Helps a achieve a more interactive communication between the reader and the author. The readers have more insight about the places in the novel and where they are located.
    
 
