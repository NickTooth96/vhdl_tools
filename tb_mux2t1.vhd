-------------------------------------------------------------------------
-- Nick Toothaker
-- Department of Electrical and Computer Engineering
-- Iowa State University
-------------------------------------------------------------------------
-- tb_mux2t1.vhd
-------------------------------------------------------------------------
-- DESCRIPTION: This file contains an implementation of a 2:1
-- mux using structural VHDL.
--
--
-- NOTES:
-- 03/15/23 by Nick Toothaker::Design created.
-------------------------------------------------------------------------

library IEEE;
use IEEE.std_logic_1164.all;

entity tb_mux2t1  is

  generic(gCLK_HPER   : time := 10 ns);

end tb_mux2t1 ;

architecture behavior of tb_mux2t1  is  
-- Calculate the clock period as twice the half-period
constant cCLK_PER  : time := gCLK_HPER * 2;


  component mux2t1 is

    port(	i_S          : in std_logic;
		i_x0         : in std_logic;
		i_x1         : in std_logic;
		o_O          : out std_logic);

  end component;

-- Temporary signals to connect to the mux2t1 component.
	
	signal si_S : std_logic;
	signal si_x0 : std_logic;
	signal si_x1 : std_logic;
	signal so_O : std_logic;


begin

test_mux2t1 : mux2t1
port map (
		i_S	=> si_S,
		i_x0	=> si_x0,
		i_x1	=> si_x1,
		o_O	=> so_O
	);

  -- This process sets the clock value (low for gCLK_HPER, then high
  -- for gCLK_HPER). Absent a "wait" command, processes restart 
  -- at the beginning once they have reached the final statement.
  P_CLK: process
  begin
    s_CLK <= '0';
    wait for gCLK_HPER;
    s_CLK <= '1';
    wait for gCLK_HPER;
  end process;
  
  -- Testbench process  
  P_TB: process

    begin

-- Test Case one
	i_S	<= '0';
	i_x0	<= '0';
	i_x1	<= '1';
	wait for cCLK_PER;

-- Test Case two
	i_S	<= '1';
	i_x0	<= '0';
	i_x1	<= '1';
	wait for cCLK_PER;

    wait;

  end process;
  
end behavior;