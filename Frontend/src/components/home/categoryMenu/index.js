import { View, Text } from 'react-native';
import React, { useState }from 'react';
import DropDownPicker from 'react-native-dropdown-picker';

export default function CategoryMenu() {

  const [open, setOpen] = useState(false);
  const [value, setValue] = useState(null);
  const [items, setItems] = useState([
    {label: 'Airline', value: 'airline'},
    {label: 'Country', value: 'country'},
    {label: 'Product', value: 'product'}
  ]);
  
  return (
    <DropDownPicker
      open={open}
      value={value}
      items={items}
      setOpen={setOpen}
      setValue={setValue}
      setItems={setItems}
      containerStyle={{
        flex:1,
        width: '50%',
        alignSelf: 'flex-start', 
        left: 35
      }}
    />
  );
}
