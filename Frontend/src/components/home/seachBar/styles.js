import { StyleSheet } from "react-native";
const styles = StyleSheet.create({
    container: {
        marginTop: 30,
        margin: 15,
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "row",
        width: "90%", 
    },
    input: {
        fontSize: 20,
        marginLeft: 10,
        width: "90%",
        paddingTop:0,
        paddingBottom:0,
      },
      searchBar__unclicked: {
        padding: 10,
        flexDirection: "row",
        width: "100%",
        backgroundColor: "#d9dbda",
        borderRadius: 20,
        alignItems: "center",
      },

      searchBar__clicked: {
        padding: 10,
        flexDirection: "row",
        width: "100%",
        backgroundColor: "#d9dbda",
        borderRadius: 20,
        alignItems: "center",
        justifyContent: "space-evenly",
      },
})
export default styles;