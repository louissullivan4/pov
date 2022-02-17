import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
    container: {
        marginTop: 30,
        height: 40,
        width: "90%",
        borderRadius: 12,
        alignSelf: "center",
        flexDirection: "row",
        alignItems: "center",
        backgroundColor: "#fdfdfd",
        shadowColor: "#757575",
        shadowRadius: 8,
        shadowOpacity: 0.3,
        shadowOffset: {
          width: 0,
          height: 3,
        },
        
    },
    textInput: {
        width: "80%",
        marginLeft: 12,
        color: "#19191a",
        borderRadius: 20,
      },

})
export default styles;