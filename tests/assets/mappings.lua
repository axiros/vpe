-- Autocreated @Sat Feb  4 22:53:26 2023 by parsing mappings.md

function TS()
	return require("telescope.builtin")
end
return {
	n = {
		["11"] = { "^", desc = "First char in line" },
		["<leader>fg"] = {
			function()
				TS().git_files()
			end,
			desc = "Git files",
		},
		["<leader>mm"] = { ":MindOpenMain<CR>", desc = "Mind Main" },
		["<leader>mp"] = { ":MindOpenSmartProject<CR>", desc = "Mind Project" },
		["<leader>d"] = { '"_d', desc = "Delete noregister" },
		["fk"] = { ":HopChar1<CR>", desc = "Hop-char" },
		["fl"] = { ":HopLine<CR>", desc = "Hop-line" },
		-- null-ls messes with formatexpr for some reason, which messes up `gq` (https://github.com/jose-elias-alvarez/null-ls.nvim/issues/1131)
		["gq"] = { "gwgw", desc = "Format w/o formatexpr" },
		[",s"] = { ":ASToggle<CR>", desc = "Toggle Autosave all buffers" },
		["<S-Tab>"] = { "zM", desc = "Close ALL Folds" },
		["<C-s>"] = { "w!", desc = "Save File" },
		[",D"] = {
			function()
				TS().diagnostics({ bufnr = 0 })
			end,
			desc = "Buffer Diagnostics",
		},
		[",C"] = {
			function()
				TS().colorscheme({ enable_preview = true })
			end,
			desc = "Color Schemes",
		},
	},
	v = {
		["<CR>"] = { "zO", desc = "Fold all open" },
		["<leader>d"] = { '"_d', desc = "Delete noregister" },
		["gq"] = { "gwgw", desc = "Format w/o formatexpr" },
	},
}
