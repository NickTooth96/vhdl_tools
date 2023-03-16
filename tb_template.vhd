-------------------------------------------------------------------------
-- CREATOR
-- Department of Electrical and Computer Engineering
-- Iowa State University
-------------------------------------------------------------------------
-- tb_NAME.vhd
-------------------------------------------------------------------------
-- DESCRIPTION
-- NOTES:
-- DATE by CREATOR::Design created.
-------------------------------------------------------------------------

LIBRARIES

entity tb_NAME  is

  GENERICS

end tb_NAME ;

architecture behavior of tb_NAME  is  
-- Calculate the clock period as twice the half-period
constant cCLK_PER  : time := gCLK_HPER * 2;


  component NAME is

    PORTS

  end component;

-- Temporary signals to connect to the NAME component.
	
SIGNALS

begin

PORTMAP
  
-- Testbench process  
  P_TB: process

    begin
TESTCASES
    wait;

  end process;
  
end behavior;