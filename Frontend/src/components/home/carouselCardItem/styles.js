import { StyleSheet, Dimensions } from "react-native";

const SLIDER_WIDTH = Dimensions.get('window').width + 80;
const ITEM_WIDTH = Math.round(SLIDER_WIDTH * 0.7);

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: "center",
        justifyContent:'center',
        borderRadius: 20,
        width: ITEM_WIDTH,
        // shadowColor: "#000",
        // shadowOffset: {
        //   width: 0,
        //   height: 5,
        // },
        // shadowOpacity: 0.29,
        // shadowRadius: 4.65,
        // elevation: 7,
      },
      image: {
        width: ITEM_WIDTH,
        height: 480,
        borderRadius: 20,
        overflow: 'hidden',
      },
      header: {
        color: "#FFF",
        fontSize: 35,
        fontWeight: "bold",
        position: "absolute",
      },
      titleContainer: {
        bottom: "55%",
        alignItems: "center",
        justifyContent:'center'
      }
})
export default styles;