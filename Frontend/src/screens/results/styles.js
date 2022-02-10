import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
    rowContainer: {
        flexDirection: 'row',
        alignItems: 'flex-start',
        backgroundColor: 'white',  
        width: '90%',
        height: 150,
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
        paddingTop: 5,
        fontSize: 15,

    }
});
export default styles;