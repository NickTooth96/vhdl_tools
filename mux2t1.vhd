-------------------------------------------------------------------------
-- Nick Toothaker
-- Cpre 381
-- Iowa State University
-------------------------------------------------------------------------


-- mux2t1.vhd
-------------------------------------------------------------------------
-- DESCRIPTION: This file contains an implementation of a 2:1
-- mux using structural VHDL.
--
--
-- NOTES:
-------------------------------------------------------------------------

library IEEE;
use IEEE.std_logic_1164.all;

entity mux2t1 is
  port(i_S          : in std_logic;
       i_x0         : in std_logic;
       i_x1         : in std_logic;
       o_O          : out std_logic);

end mux2t1;

architecture structural of mux2t1 is

  component andg2 is
    port(	i_A          : in std_logic;
       		i_B          : in std_logic;
       		o_F          : out std_logic);
  end component;

  -- Signal to store output of first and_0
  signal out_and_0         	: std_logic;
  -- Signal to store output of first and_1
  signal out_and_1  		: std_logic;
  -- Signal to store output of first not_0
  signal out_not_0       	: std_logic;

begin

  ---------------------------------------------------------------------------
  not_0: invg
    port Map(	i_A    	     => i_S,
		o_F   	     => out_not_0);
-- block start
--   add_0: andg2
--     port MAP( 	i_A          => i_x0,
--        		i_B          => out_not_0,
--        		o_F          => out_and_0);
-- 
--   add_1: andg2
--     port MAP( 	i_A          => i_S,
--        		i_B          => i_x1,
--        		o_F          => out_and_1);
-- 		block end
  or_0: org2
    port MAP( 	i_A          => out_and_0,
       		i_B          => out_and_1,
       		o_F          => o_O;

  
end structural;


