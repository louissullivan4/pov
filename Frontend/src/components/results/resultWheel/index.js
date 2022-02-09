import { View, Text } from 'react-native';
import React from 'react';
import AnimatedProgressWheel from 'react-native-progress-wheel';
import styles from './styles';

export default function ResultsWheel(props) {
  return (
        <View style={{position: 'relative', }}>
          <AnimatedProgressWheel 
              width={100}
              size={160}
              animateFromValue={0}
              progress={props.rating}
              backgroundColor={'#c8e8df'}
              duration={2000}
              color={'#8fcdba'}
          />
          <Text style={{position: 'absolute', alignSelf:'center', bottom:46, fontSize: 55, color:'#6e867f'}}>{props.rating}</Text>
        </View>

  );
}
