import { StyleSheet } from "react-native";
import { Platform } from "react-native";

const styles = StyleSheet.create({

    container: {
        flex:1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: "#FFF"
    },
    // buttonContainer: {
    //     flexDirection: 'row',
    //     flex:1,
    //     justifyContent: "flex-start",
    //     alignItems: "center",
    //     ...(Platform.OS !== 'android' && {
    //         zIndex: 10
    //       }),
    
    // },
    // button: {
    //     backgroundColor: "#c8e8df",
    //     borderRadius: 20,
    //   ,  padding: 5
    // }
})
export default styles;