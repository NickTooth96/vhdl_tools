# Blockcom

A small tool to add block comments to VHDL files.

Written by Nick Toothaker

February 2023

Last Update: 2/25/2023

## Getting Started

To use this tool simply clone it into the folder where you are working with VHDL file. This will create a folder called blockcom. The folder contains the program files for blockcom.py, you will not need to open this folder.

blockcom runs as a CLI so you can use it from the terminal. To use blockcom type the following into the terminal you used to clone the repository: 

```python3 ./blockcom/blockcom.py --Help```

This will display the help page for blockcom. The help page should explain the tool well enough but if you are impatient, you can follow the steps in next section. 

## Quick Start 

### Comment Out Lines

To add block comments to a VHDL file follow these steps.

1. Open a terminal in the root directory of your VHDL project.
1. Open the `.vhd` file you want to add comments to.
1. At the empty line where you want the block comment to begin type `block start`
1. At the empty line where you want to end the block comment type `block end` see the example below:

    ```  
        s_s     <= "00000";
        wait for cCLK_PER;
       
        s_s     <= "00000";
        wait for cCLK_PER;
    block start
        s_s     <= "00001";
        wait for cCLK_PER;
  
        s_s     <= "00010";
        wait for cCLK_PER;
    block end

1. Open the terminal and run the following command 
`python3 ./blockcom/blockcom.py -c [filepath]`
where `[filepath]` is the name of the `.vhd` file that you are using with the relative path from `file.vhd` to blockcom. 
1. blockcom will parse through the given file and print "File Processed" to the command line. 

### Uncomment

To remove block comments, you have placed in a VHDL file follow these steps. 

1. Open a terminal in the root directory of your VHDL project and run the following command 
`python3 ./blockcom/blockcom.py -u [filepath]`
where `[filepath]` is the name of the `.vhd` file that you are using with the realative path from blockcom to `file.vhd`.
1. blockcom will parse through the given file and print "File Processed" to the command line.

### Removing existing Block Comments

To remove block comments that blockcom did not create you have to prepare the file by adding appropriate block flags. Go to the first line of the block comment you want to remove, and change it as shown:

| Original | New |
| :--- | :--- |
|| 1 -- block start |
|1  -- code line 1 | 2 -- code line 1 |
|2  -- code line 2 | 3 -- code line 2 |
|3  -- code line 3  | 4 -- code line 3 |
|| 5 -- block end |

**NOTE:** Make sure that block flags are the only text on a line.

1. Open a terminal in the root directory of your VHDL project and run the following command
`python3 ./blockcom/blockcom.py -u [filepath]`
where `[filepath]` is the name of the `.vhd` file that you are using with the realative path from blockcom to `file.vhd`.
1. blockcom will parse through the given file and print "File Processed" to the command line.
