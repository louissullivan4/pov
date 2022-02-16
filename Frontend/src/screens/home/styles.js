import { StyleSheet } from "react-native";
import { Platform } from "react-native";

const styles = StyleSheet.create({

    container: {
        flex:1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: "#FFF"
    },
    
    title: {
        top: 50,
        right: 100,
        color: '#6e867f',
        
    },

    titleText: {
        fontSize: 25,
        fontStyle: 'italic',
    }
})
export default styles;