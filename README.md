# Nuke Auto Comp

> Auto comp is a Nuke tool that automatically creates a composition node graph.

## How to install

You will need some files that several Illogic tools need. You can get them via this link :
https://github.com/Illogicstudios/common

---

## Features

### Auto Comp

Choose the shot to process

<div align="center">
  <span>
    <img src="https://github.com/Illogicstudios/auto_comp/assets/94440879/c8105733-49af-4816-bcb8-7190dd79a583" width=80%>
  </span>
  <br/>
</div>

We can select the shot path in the user interface. The shot folder has to contain a folder named render_out.

Select the Unpack Mode that suits you

<div align="center">
  <span>
    <img src="https://github.com/Illogicstudios/auto_comp/assets/94440879/4babed4c-8ef7-4407-9fd4-41196837220b" width=25%>
  </span>
  <br/>
</div>

Visualize the layer that are supported by the mode selected

<div align="center">
  <span>
    <img src="https://github.com/Illogicstudios/auto_comp/assets/94440879/d7dc13f2-cf7a-4e72-b10d-4fb28e1b9b36" width=60%>
  </span>
  <br/>
</div>

Press the Auto Comp button To automatically generate the composition graph nodes.

### Shuffle Layer

Visualize the layer of the selected shot

<div align="center">
  <span>
    <img src="https://github.com/Illogicstudios/auto_comp/assets/94440879/80123cfa-ffb1-4202-bc65-8c5d7db31b45" width=55%>
  </span>
  <br/>
</div>

Select layers and press the Shuffle selected layer button to generate the shuffled layer.

### Shuffle Read Channel

Select a Read in the graph node then select all the channels that have to be shuffled in the list then press Shuffle selected channels button

<div align="center">
  <span>
    <img src="https://github.com/Illogicstudios/auto_comp/assets/94440879/6ff84779-d303-43f7-add4-389ff2cec33b" width=70%>
  </span>
  <br/>
</div>

### Update Reads

Visualize the version of each layer in the scene. Update to the last version by selecting the layers that have to be shuffled and pressing the Update selected read nodes button

<div align="center">
  <span>
    <img src="https://github.com/Illogicstudios/auto_comp/assets/94440879/97054211-6487-47ea-904a-b4c5203eb2a5" width=70%>
  </span>
  <br/>
</div>

---

## How to add a new Unpack mode

To Add a new Unpack mode you have to create a new config file in the `/mode/` folder.

Here are all the fields in the config file :

* The name of the mode to be created.
```json
"name": "Unpack Mode Name",
```
<br/>

* Layers to be retrieved.  Each layer has :
  * a name (useful for differentiating them in rules and for the user interface)
  * a regular expression (regexp) to retrieve the folder
  * a group operation useful if there are multiple layers that valid the regexp to merge them
  * some useful aliases for creating more universal rules
  * an array of options to specify some parameters like the color of the backdrops
```json
"layers": [
    {
      "name": "NAMELAYER1",
      "rule": "^regex_layer1$",
      "group_operation": "over",
      "aliases": ["CURRENT"],
      "options": {"color": [55, 55, 150]}
    },
    {
      "name": "NAMELAYER2",
      "rule": "^regex_layer2$",
      "group_operation": "over",
      "aliases": ["CURRENT"],
      "options": {"color": [140, 50, 125]}
    },
    {
      "name": "NAMELAYER3",
      "rule": "^regex_layer3$",
      "group_operation": "over",
      "aliases": ["CURRENT"],
      "options": {"color": [140, 50, 125]}
    }
  ]
```
<br/>

- Layers that need to be shuffled.
```json
"shuffle": {
  "shuffle_layer": [
    "NAMELAYER1", "NAMELAYER2"
  ]
}
```
<br/>

* Rules for the merging part. Each rule is tested in the order of the array. if the element `a` is present and if the element `b` is present, consume them to create the `result` with the `operation`. The `result` is facultative.
```json
"merge": {
  "rules": [
    {
      "a": "NAMELAYER1",
      "b": "NAMELAYER2",
      "operation": "over",
      "result": "CURRENT"
    },
    {
      "a": "NAMELAYER3",
      "b": "CURRENT",
      "operation": "plus",
      "result": "CURRENT"
    }
  ]
}
```
