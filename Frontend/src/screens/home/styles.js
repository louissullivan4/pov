import { StyleSheet } from "react-native";

// const styles = StyleSheet.create({

//     container: {
//         flex:1,
//         flexDirection: "column",
//         justifyContent: "center",
//         alignItems: "center",
//         backgroundColor: "#FFF",
//     },
//     navigationContainer: {
//         flexDirection: "row"
//     },
//     category: {
//     },
//     button: {
//     }
// })
// export default styles;

const styles = StyleSheet.create({

    container: {
        flex:1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: "#FFF"
    },
    buttonContainer: {
        zIndex: 10,
        flexDirection: "row",
        backgroundColor: "#FFF",
    },
    category: {
        width: "85%"
    },
    button: {
        right: 70,
        backgroundColor: "#c8e8df",
        borderRadius: 5,
        padding: 5
    }
})
export default styles;