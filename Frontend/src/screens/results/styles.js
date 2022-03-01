import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
    rowContainer: {
        flexDirection: 'row',
        alignItems: 'flex-start',
        backgroundColor: 'white',  
        width: '90%',
        alignSelf: 'center',
        borderRadius: 20, 
        marginTop: 20,  
        backgroundColor: '#c8e8df',
    },
    container: {
        flex:1,
        alignItems:'center',
        justifyContent: 'flex-start',
        backgroundColor:'white',
    },
    text: {
        paddingTop: 10,
        fontSize: 15,
    },
    textlist:{
        paddingTop: 5,
        fontSize: 15,
    },
    urltext: {
        color: "dodgerblue",
        textDecorationLine: 'underline'
    }
});
export default styles;