# NOVEL MAP CUSTOMIZER

#### Description:
  This helps authors to customize the maps for their novel specifying where a particular place is located on the map.
  They can specify areas , pinpoint locations and describe each of these places to readers intrested in gaining more insight about places in the book
  they are reading .
  The geospartial elements are stored using postgis (a spatial database extender for PostgreSQL). The map is rendered with a javascript library using leaflet ,the
  controllers(backend) is handled with django and django restframework for its api. The djangorestframework helps with easy parsing and representation of the locations in geojson.
### Design
#  The model file creates a database for the author , Book and the locations for the map points to be stored.
    The Author stores the name of the author and associates the user to it as foreignkey
    The Novel Table stores the title of the book , associates with the author through primary key , and stores the url to the map of the book
    The Maptype Table is used to store the type of the map's point location (e.g if its a tower , fotress ...etc) it also stores the primary key of the novel
    The Marker Table stores the location coordinate of the point  , also the primary key that stores the type of the map, the description of the coordinate point.
    The Area Table stores the Areas on the map
# The url controls the path to access the resources
  1. the default url shows the link to the map page where all the novels are displayed
  2. the map url routes the link to the home page
  3. the point url controls the link to the point page where all the coordinates of the map are represented
  4. the sore endpoint is the url that allows the storage of the coordinates for a particular novel

# The view on the other hand acts as the controller , this is where the logic resides and the files accepted are handled.
  1. this consists:
   -the home function which selects all the books from the database and sends them to the "first.html" page .
   -the index function controls the storage of the maptypes , it also displays the types of the map point for a particular novel and sends it into the
  "index.html" page
   -the store_points function stores the coordinates by listening for ajax and post request and sending the request to the form to handle the parsing , it returns error if it failed and success if it succeds
   -the display querys the database for all the points (marker) of that particular novel having a specific type and sends it to the "secound.html"

#  The forms allows to validate the submitted user input and allows for easy storage of these inputs.
  1. The PointForm class parses the map submitted and make it an appropriate point field . stores it when the store function is called on the instance
  2. The MapForm takes the submitted type and stores the instance to the database when the save method is called .

#  The Serializer serializes the instance to passed it.
  1. MarkerSerializer , serializes the map instance and represents the point coordinate in  geojson , a format for map rendering

# The static Folder stores the static files
  1. the css files
  2. the png images (leaf-red, leaf-shadow )to be represented on the map points

# The Template Folder stores the html files to be served
  1. layout.html , this is used to minimize recurring code and html header , its extended in other files .
  2. first.html extends the layout.html file and displays all the book's title and link to create its map and view its map
  3. index.html extends the layout.html displays the type and a form to make a post request to store the maptype
  4. secound.html renders the map and use the leaflet library to put the coordinates on the map also uses a javascript to make an ajax request to store these points indicated(coordinates)

### JAVASCRIPT LIBRARIES
  leaflet library helps handle the map rendering and basic event listeners .
  boostrap  is used for the design in place of oveload css.


 ### Why Build This ?
    Helps a achieve a more interactive communication between the reader and the author. The readers have more insight about the places in the novel and where they are located.




